# ZDI-11-036: IBM DB2 db2dasrrm receiveDASMessage Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-036
- **ZDI-CAN:** ZDI-CAN-776
- **Date:** 2011-01-31
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** IBM
- **Affected Products:** DB2 Universal Database
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-036/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM DB2. Authentication is not required to exploit this vulnerability. The flaw exists within the db2dasrrm component which listens by default on TCP port 524. When allocating a buffer within receiveDASMessage a user supplied length is used as a parameter to malloc(). This buffer is later copied into without any bounds checking and can be made to overflow. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the das user user.

## Additional Details

v9.1 fp10 IC71203 https://www-304.ibm.com/support/entdocview.wss?uid=swg1IC71203 v9.5 fp7 IC72028 https://www-304.ibm.com/support/entdocview.wss?uid=swg1IC72028 v9.7 fp3a IC72029 https://www-304.ibm.com/support/entdocview.wss?uid=swg1IC72029

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2011-01-31 - Coordinated public release of advisory
