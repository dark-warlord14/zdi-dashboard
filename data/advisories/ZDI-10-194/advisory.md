# ZDI-10-194: IBM Tivoli Provisioning Manager for OS Deployment TCP to ODBC Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-194
- **ZDI-CAN:** ZDI-CAN-781
- **Date:** 2010-10-08
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Provisioning Manager
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-194/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary SQL queries on vulnerable installations of Tivoli Provisioning Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TCP to ODBC gateway component which listens by default on TCP port 2020. Authentication is not required to issue SQL queries to the service. A remote attacker can abuse this to read, modify, or create records within the database.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://publib.boulder.ibm.com/infocenter/tivihelp/v3r1/index.jsp?topic=%2Fcom.ibm.tivoli.tpm.osd.doc%2Finstall%2Ftosd_setmsacessdbpwd.html

## Disclosure Timeline

- 2010-07-06 - Vulnerability reported to vendor
- 2010-10-08 - Coordinated public release of advisory
