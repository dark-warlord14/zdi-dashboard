# ZDI-17-165: Hewlett Packard Enterprise Intelligent Management Center FileDownloadServlet fileName Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-165
- **ZDI-CAN:** ZDI-CAN-4053
- **Date:** 2017-03-11
- **CVE:** CVE-2017-5795
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-165/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within FileDownloadServlet. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03714en_us

## Disclosure Timeline

- 2016-10-17 - Vulnerability reported to vendor
- 2017-03-11 - Coordinated public release of advisory
