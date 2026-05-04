# ZDI-18-154: Apple iOS backboardd Double Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-154
- **ZDI-CAN:** ZDI-CAN-5354
- **Date:** 2018-02-07
- **CVE:** CVE-2017-7162
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** iOS
- **Credit:** 360 Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-154/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple iOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the backboardd service. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208334

## Disclosure Timeline

- 2017-11-02 - Vulnerability reported to vendor
- 2018-02-07 - Coordinated public release of advisory
- 2018-02-07 - Advisory Updated
