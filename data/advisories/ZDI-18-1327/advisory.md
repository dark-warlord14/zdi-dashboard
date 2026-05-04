# ZDI-18-1327: Apple macOS libATSServer Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1327
- **ZDI-CAN:** ZDI-CAN-6360
- **Date:** 2018-10-30
- **CVE:** CVE-2018-4411
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** lilang wu moony Li of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1327/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the FODBWriteToAnnex method. The issue lies in the failure to properly validate the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-07-12 - Vulnerability reported to vendor
- 2018-10-30 - Coordinated public release of advisory
- 2018-10-30 - Advisory Updated
