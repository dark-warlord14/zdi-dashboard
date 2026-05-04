# ZDI-17-830: Hewlett Packard Enterprise Intelligent Management Center mibFileServlet Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-830
- **ZDI-CAN:** ZDI-CAN-4837
- **Date:** 2017-10-03
- **CVE:** CVE-2017-12554
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-830/
## Vulnerability Details

This vulnerability allows remote attackers to rename arbitrary files on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the mibFileServlet servlet, which listens on TCP ports 8080 and 8443 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03782en_us

## Disclosure Timeline

- 2017-05-30 - Vulnerability reported to vendor
- 2017-10-03 - Coordinated public release of advisory
