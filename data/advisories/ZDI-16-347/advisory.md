# ZDI-16-347: Apple OS X IOAudioFamily Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-347
- **ZDI-CAN:** ZDI-CAN-3603
- **Date:** 2016-05-19
- **CVE:** CVE-2016-1820
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Jack Tang and Moony Li of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-347/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the IOAudioFamily kernel extension. The issue lies in the failure to validate a user-supplied size prior to copying data into a kernel buffer. A local attacker can leverage this vulnerability to escalate privileges and execute code within the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206567

## Disclosure Timeline

- 2016-03-11 - Vulnerability reported to vendor
- 2016-05-19 - Coordinated public release of advisory
