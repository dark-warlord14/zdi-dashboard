# ZDI-14-371: (0Day) Denon AVR-3313CI 'Friendlyname' Persistent Cross-Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-371
- **ZDI-CAN:** ZDI-CAN-2333
- **Date:** 2014-11-03
- **CVE:** CVE-2014-8508
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:N
- **Affected Vendors:** Denon
- **Affected Products:** AVR-3313CI
- **Credit:** Ricky "HeadlessZeke" Lawshae of HP DVLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-371/
## Vulnerability Details

This vulnerability allows remote attackers to insert persistent JavaScript on vulnerable installations of the Denon AVR-3313CI audio/video receiver's web portal. Authentication is not required to persist the attack. However, user interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within parameters used by s_network.asp which does not properly sanitize user-supplied data. Some parameter values are used on multiple pages and the injected JavaScript will therefore run when any user views any of those pages, including the portal's landing page.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. 08/13/2014 - ZDI contacted Denon's Live Support Chat requested a PGP and secure email, but was ultimately disconnected 08/13/2014 - ZDI sent email follow-up to Denon Support 08/19/2014 - ZDI sent email follow-up to Denon Support 09/04/2014 - ZDI sent email follow-up to Denon Support -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines and disable the feature when the receiver is not in use. It can be turned off when in standby mode by following these instructions: Press MAIN to switch the zone to the MAIN ZONE. Press SETUP. Select 'IP Control'. Change setting to 'Off in Standby'

## Disclosure Timeline

- 2014-08-13 - Vulnerability reported to vendor
- 2014-11-03 - Coordinated public release of advisory
