# ZDI-25-096: PostHog slack_incoming_webhook Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-096
- **ZDI-CAN:** ZDI-CAN-25352
- **Date:** 2025-02-25
- **CVE:** CVE-2025-1521
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** PostHog
- **Affected Products:** PostHog
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-096/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of PostHog. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of the slack_incoming_webhook parameter. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

PostHog has issued an update to correct this vulnerability. More details can be found at: https://github.com/PostHog/posthog/commit/6e8f035f9acd339c5ba87ba6ea40fc1ab3053d42

## Disclosure Timeline

- 2024-10-03 - Vulnerability reported to vendor
- 2025-02-25 - Coordinated public release of advisory
- 2025-02-25 - Advisory Updated
