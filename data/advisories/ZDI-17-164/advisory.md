# ZDI-17-164: Hewlett Packard Enterprise Intelligent Management Center FileUploadServlet Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-164
- **ZDI-CAN:** ZDI-CAN-4055
- **Date:** 2017-03-11
- **CVE:** CVE-2017-5794
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-164/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within FileUploadServlet. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03715en_us

## Disclosure Timeline

- 2016-10-17 - Vulnerability reported to vendor
- 2017-03-11 - Coordinated public release of advisory
