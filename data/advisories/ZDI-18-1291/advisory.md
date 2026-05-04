# ZDI-18-1291: Apple macOS getsockopt Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1291
- **ZDI-CAN:** ZDI-CAN-6203
- **Date:** 2018-10-17
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** juwei lin (@panicaII) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1291/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the getsockopt system call. The issue results from the lack of validating that user-supplied options are of the appropriate size. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code under the context of the kernel.

## Additional Details

This issue was addressed with macOS High Sierra 10.13.6, iOS 11.4.1, tvOS 11.4.1, and watchOS 4.3.2.

## Disclosure Timeline

- 2018-05-18 - Vulnerability reported to vendor
- 2018-10-17 - Coordinated public release of advisory
- 2018-10-17 - Advisory Updated
