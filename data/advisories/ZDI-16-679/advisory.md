# ZDI-16-679: Apple iOS legacy-diagnostics Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-679
- **ZDI-CAN:** ZDI-CAN-3954
- **Date:** 2017-03-31
- **CVE:** CVE-2016-7630
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** iOS
- **Credit:** 7cd6cbc56470722cd7dea01561796431
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-679/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Apple iOS. User interaction is required to exploit this vulnerability in that the target must connect to a WiFi access point. The specific flaw exists within the usage of the legacy-diagnostics protocol handler. The issue lies in the launching of a diagnostic application that is able to render webpages outside of the sandbox. An attacker can leverage this vulnerability to escalate privileges outside the context of the sandbox.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT207422

## Disclosure Timeline

- 2016-08-30 - Vulnerability reported to vendor
- 2017-03-31 - Coordinated public release of advisory
