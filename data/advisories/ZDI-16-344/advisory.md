# ZDI-16-344: Apple OS X DTrace Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-344
- **ZDI-CAN:** ZDI-CAN-3564
- **Date:** 2016-05-19
- **CVE:** CVE-2016-1826
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-344/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the dtrace facility. The issue lies with the failure to validate user-supplied chunk size values which can lead to arbitrary read and write of memory. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT201222

## Disclosure Timeline

- 2016-02-12 - Vulnerability reported to vendor
- 2016-05-19 - Coordinated public release of advisory
