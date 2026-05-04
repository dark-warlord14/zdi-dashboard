# ZDI-14-386: ManageEngine OpUtils ConfigSaveServlet saveFile Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-386
- **ZDI-CAN:** ZDI-CAN-2428
- **Date:** 2014-11-21
- **CVE:** CVE-2014-8678
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** ManageEngine
- **Affected Products:** OpUtils
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-386/
## Vulnerability Details

This vulnerability allows remote attackers to disclose files on vulnerable installations of ManageEngine OpUtils. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the ConfigSaveServlet servlet. The issue lies in the failure to properly sanitize a filename. A remote attacker can exploit this vulnerability to disclose files from the system.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://uploads.zohocorp.com/Internal_Useruploads/OpUtils/p192eqio4tq021kpk17q58jgqvm0/ManageEngine_OpUtils_71024.ppm

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2014-11-21 - Coordinated public release of advisory
