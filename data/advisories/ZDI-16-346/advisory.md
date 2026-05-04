# ZDI-16-346: (Pwn2Own) Apple OS X SubmitDiagInfo Arbitrary Directory Creation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-346
- **ZDI-CAN:** ZDI-CAN-3607
- **Date:** 2016-05-19
- **CVE:** CVE-2016-1806
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** lokihardt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-346/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the com.apple.SubmitDiagInfo service. The issue lies in the failure to validate a user-supplied path prior to creating a directory. An attacker can leverage this vulnerability to escalate privileges and execute code as root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206567

## Disclosure Timeline

- 2016-03-16 - Vulnerability reported to vendor
- 2016-05-19 - Coordinated public release of advisory
