# ZDI-15-291: SQLite Default Value Authorization Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-291
- **ZDI-CAN:** ZDI-CAN-2901
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3659
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SQLite
- **Affected Products:** SQLite
- **Credit:** Peter Rutenbar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-291/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SQLite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of DEFAULT expressions for column values. The issue lies in the ability to create a table that will execute privileged functions by specifying a DEFAULT value for a column and then inserting into the table. An attacker can leverage this vulnerability to execute restricted SQL statements under the context of the current process.

## Additional Details

SQLite has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2015-05-18 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
