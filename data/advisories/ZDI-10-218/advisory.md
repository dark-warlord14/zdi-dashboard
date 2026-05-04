# ZDI-10-218: IBM DB2 install_jar Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-218
- **ZDI-CAN:** ZDI-CAN-743
- **Date:** 2010-10-19
- **CVE:** CVE-2008-2154
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** DB2 Universal Database
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-218/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM DB2. Authentication is required in that a user must have the ability to connect to the database. The specific flaw exists within the install_jar procedure. The install_jar procedure contains a directory traversal vulnerability that will allow the attacker to upload a Jar file to a directory outside of the intended "\function\jar\Name_of_logged_user\" directory. A remote attacker can abuse this to execute arbitrary code under the context of the current user.

## Additional Details

IZ21983: http://www-01.ibm.com/support/docview.wss?uid=swg1IZ21983 IZ22143: http://www-01.ibm.com/support/docview.wss?uid=swg1IZ22143

## Disclosure Timeline

- 2010-06-17 - Vulnerability reported to vendor
- 2010-10-19 - Coordinated public release of advisory
