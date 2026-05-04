# ZDI-20-571: LAquis SCADA LGX File Insufficient UI Warning Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-571
- **ZDI-CAN:** ZDI-CAN-10317
- **Date:** 2020-04-30
- **CVE:** CVE-2020-10618
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** LAquis
- **Affected Products:** SCADA
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-571/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of LAquis SCADA. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the AddComboFile method when processing LGX files. When opening an LGX file, the user interface fails to warn the user of unsafe actions. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

LAquis has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-119-01

## Disclosure Timeline

- 2020-02-20 - Vulnerability reported to vendor
- 2020-04-30 - Coordinated public release of advisory
