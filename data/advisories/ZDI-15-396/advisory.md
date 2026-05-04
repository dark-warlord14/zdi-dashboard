# ZDI-15-396: ManageEngine Service Desk File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-396
- **ZDI-CAN:** ZDI-CAN-2709
- **Date:** 2015-08-20
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** ManageEngine
- **Affected Products:** ServiceDesk
- **Credit:** Pedro Ribeiro (pedrib@gmail.com) / Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-396/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ManageEngine ServiceDesk. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of uploaded files. The issue lies in the ability to use directory traversal to extract a ZIP file to an arbitrary location. An attacker can leverage this vulnerability to execute code under the context of the user running the vulnerable service.

## Additional Details

The vulnerability was fixed in 9103 build which was released on July 23rd 2015.

## Disclosure Timeline

- 2015-06-03 - Vulnerability reported to vendor
- 2015-08-20 - Coordinated public release of advisory
