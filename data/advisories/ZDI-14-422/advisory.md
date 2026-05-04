# ZDI-14-422: ManageEngine NetFlow Analyzer CollectorConfInfoServlet COLLECTOR_ID Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-422
- **ZDI-CAN:** ZDI-CAN-2462
- **Date:** 2014-12-11
- **CVE:** CVE-2014-9373
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ManageEngine
- **Affected Products:** NetFlow Analyzer
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-422/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ManageEngine NetFlow Analyzer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CollectorConfInfoServlet servlet. The issue lies in the failure to sanitize the filenames uploaded to the servlet. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://uploads.zohocorp.com/Internal_Useruploads/dnd/NetFlow_Analyzer/p1982sg3vuo9pibt15p01uju1hv0/consolidated_1Dec.zip

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2014-12-11 - Coordinated public release of advisory
