# ZDI-14-420: ManageEngine Desktop Central MSP NativeAppServlet UDID JSON Object Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-420
- **ZDI-CAN:** ZDI-CAN-2445
- **Date:** 2014-12-11
- **CVE:** CVE-2014-9371
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ManageEngine
- **Affected Products:** Destkop Central MSP
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-420/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ManageEngine Desktop Central MSP. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NativeAppServlet servlet. The issue lies in the failure to sanitize JSON data before processing it. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://uploads.zohocorp.com/Internal_Useruploads/Desktop_Central/p195gob20s1pas1fnv1qb9j3bvng0/ManageEngine_Desktop_Central_MSP_9_0_SP-0_75.ppm

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2014-12-11 - Coordinated public release of advisory
