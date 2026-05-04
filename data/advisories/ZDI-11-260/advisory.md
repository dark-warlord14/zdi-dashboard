# ZDI-11-260: Nortel Media Application Server cstore.exe cs_anams Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-260
- **ZDI-CAN:** ZDI-CAN-1096
- **Date:** 2011-08-16
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Nortel
- **Affected Products:** Media Application Server
- **Credit:** AbdulAziz Hariri of ThirdEyeTesters
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-260/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Nortel Media Application Server. Authentication is not required to exploit this vulnerability. The flaw exists within the cstore.exe component which listens by default on TCP port 52005. When handling a CONTENT_STORE_ADMIN_REQ packet type the process trusts length value provided by the 'cs_anams' parameter and blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Nortel has issued an update to correct this vulnerability. More details can be found at: https://support.avaya.com/css/P8/documents/100146108

## Disclosure Timeline

- 2011-02-17 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory
