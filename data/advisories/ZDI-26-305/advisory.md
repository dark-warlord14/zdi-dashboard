# ZDI-26-305: (0Day) OpenAI Codex Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-305
- **ZDI-CAN:** ZDI-CAN-29475
- **Date:** 2026-04-28
- **CVE:** N/A
- **CVSS:** 8.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** OpenAI
- **Affected Products:** Codex
- **Credit:** Peter Girnus (@gothburz), Demeng Chen (@DemengChen233), Project AESIR with TrendAI Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-305/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the sandbox on affected installations of OpenAI Codex. User interaction is required to exploit this vulnerability in that the target must use Codex to process a repository containing malicious JavaScript. The specific flaw exists within the JavaScript execution environment. The issue results from the lack of proper isolation of the sandboxed context. An attacker can leverage this vulnerability to bypass the sandbox and execute code in the context of the current user.

## Additional Details

02/24/26 - ZDI reported the vulnerability to the vendor 02/25/26 - the vendor acknowledged the receipt of the report 03/05/26 - the vendor requested technical clarification 03/09/26 - ZDI provided additional details 04/06/26 - the vendor communicated they were able to reproduce the reported behavior 04/13/26 - the vendor rejected vulnerability for being out of scope for their bug bounty program 04/13/26 - ZDI confirmed not accepting any rewards or bounties and asked for the fix date 04/13/26 - the vendor stated that the vulnerability was not in the default Codex product surface 04/17/26 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2026-02-24 - Vulnerability reported to vendor
- 2026-04-28 - Coordinated public release of advisory
- 2026-04-28 - Advisory Updated
