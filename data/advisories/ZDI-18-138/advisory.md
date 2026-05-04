# ZDI-18-138: Hewlett Packard Enterprise Intelligent Management Center redirectviewer Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-138
- **ZDI-CAN:** ZDI-CAN-4905
- **Date:** 2018-01-25
- **CVE:** CVE-2017-8983
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-138/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the parafile parameter provided to the redirectviewer servlet. When parsing this parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03808en_us

## Disclosure Timeline

- 2017-07-10 - Vulnerability reported to vendor
- 2018-01-25 - Coordinated public release of advisory
- 2018-01-25 - Advisory Updated
