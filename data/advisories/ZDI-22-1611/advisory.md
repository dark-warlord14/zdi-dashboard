# ZDI-22-1611: ManageEngine ServiceDesk Plus invokeDataUploadTool Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1611
- **ZDI-CAN:** ZDI-CAN-18260
- **Date:** 2022-11-21
- **CVE:** CVE-2022-40770
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** ServiceDesk Plus
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1611/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ManageEngine ServiceDesk Plus. Authentication is required to exploit this vulnerability. The specific flaw exists within the invokeDataUploadTool function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/products/service-desk/CVE-2022-40770.html

## Disclosure Timeline

- 2022-08-10 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory
