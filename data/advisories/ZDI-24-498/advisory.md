# ZDI-24-498: NETGEAR ProSAFE Network Management System UpLoadServlet Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-498
- **ZDI-CAN:** ZDI-CAN-22923
- **Date:** 2024-05-22
- **CVE:** CVE-2024-5247
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-498/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NETGEAR ProSAFE Network Management System. Authentication is required to exploit this vulnerability. The specific flaw exists within the UpLoadServlet class. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000066165/Security-Advisory-for-Missing-Function-Level-Access-Control-on-the-NMS300-PSV-2024-0005

## Disclosure Timeline

- 2024-01-11 - Vulnerability reported to vendor
- 2024-05-22 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
