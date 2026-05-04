# ZDI-18-1334: Apple macOS sysctl_procargsx Uninitialized Buffer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1334
- **ZDI-CAN:** ZDI-CAN-6839
- **Date:** 2018-10-31
- **CVE:** CVE-2018-4413
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Juwei Lin(@panicaII) of TrendMicro Mobile Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1334/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the sysctl_procargsx system call. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-07-20 - Vulnerability reported to vendor
- 2018-10-31 - Coordinated public release of advisory
