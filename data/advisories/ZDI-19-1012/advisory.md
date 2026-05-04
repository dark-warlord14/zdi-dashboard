# ZDI-19-1012: (0Day) Linux Kernel proc stat Improper Access Control Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1012
- **ZDI-CAN:** ZDI-CAN-7607
- **Date:** 2019-12-12
- **CVE:** N/A
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Federico Bento
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1012/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of the Linux kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the logic that controls access to the /proc/<pid>/stat file. Access is not properly restricted from unauthorized processes, which can result in disclosure of useful memory addresses. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 06/04/19 – ZDI provided the vulnerability report to the vendor 06/04/19 – The vendor acknowledged receipt of the report 09/13/19 – ZDI requested an update 09/23/19 – The vendor replied that they were investigating the status 09/25/19 – The vendor engineer confirmed the investigation was active 10/08/19 - ZDI requested an update 10/22/19 - ZDI requested an update 11/21/19 – The vendor engineered verified the issue, exists but did not indicate commitment to fix 11/21/19 – ZDI requested an ETA 11/22/19 – The vendor replied they feel it is “more of a kernel hardening issue” and confirmed commitment to patch the following week 11/24/19 – ZDI agreed to wait 11/27/19 – The vendor replied that they have located an optional configuration remediation already implemented and will not do further patching/remediation at this time 12/10/19 – ZDI advised the vendor of the intention to publish the report as 0-day on 12/12/19 -- Mitigation: Use the hidepid mount(8) parameter to mitigate this issue.

## Disclosure Timeline

- 2019-06-04 - Vulnerability reported to vendor
- 2019-12-12 - Coordinated public release of advisory
