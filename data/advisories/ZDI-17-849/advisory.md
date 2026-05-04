# ZDI-17-849: Hewlett Packard Enterprise Intelligent Management Center flexFileUpload Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-849
- **ZDI-CAN:** ZDI-CAN-4758
- **Date:** 2017-11-06
- **CVE:** CVE-2017-8961
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-849/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be easily bypassed. The specific flaw exists within the flexFileUpload servlet, which listens on TCP port 8080 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute arbitrary code under the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03788en_us

## Disclosure Timeline

- 2017-05-12 - Vulnerability reported to vendor
- 2017-11-06 - Coordinated public release of advisory
