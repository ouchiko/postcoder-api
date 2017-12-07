import sqlite3

class PostcodeSearch:
    def __init__(self, dbfile):
        self.dbfile = dbfile

    def setPostcode(self, partial_postcode):
        status = True
        tmp_postcode = ''.join(x for x in partial_postcode if (x.isalpha() or x.isnumeric()))
        tmp_postcode = tmp_postcode.replace(" ","")
        if tmp_postcode == '':
            return {'error':'invalid postcode requested'}
        if len(tmp_postcode)<4:
            return {'error':'postcode is too short, 4 min'}
        #tmp_postcode = tmp_postcode[:len(tmp_postcode)-3] + " " + tmp_postcode[-3:]
        self.postcode = tmp_postcode.upper()
        print "Requested Postcode String: %s" % (tmp_postcode)
        return status

    def search(self):
        rows = []
        con = sqlite3.connect(self.dbfile)
        cursor = con.execute(
            "SELECT textValue, lat, lng, address1, address2, address3, address4, address5 FROM postcodes WHERE textValue like (?)",
            (self.postcode+'%',)
        )
        for row in cursor:
            strut = {
                'lat': row[1],
                'lng': row[2],
                'address': {
                    'address1': row[3],
                    'address2': row[4],
                    'address3': row[5],
                    'area': row[6],
                    'country': row[7],
                    'postcode': row[0][:len(row[0])-3] + " " + row[0][-3:]
                }
            }
            rows.append(strut)

        #print rows;
        con.close()
        return {'search':self.postcode, 'data':rows}
