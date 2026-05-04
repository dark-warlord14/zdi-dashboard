# ZDI-25-097: PostHog database_schema Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-097
- **ZDI-CAN:** ZDI-CAN-25358
- **Date:** 2025-02-25
- **CVE:** CVE-2025-1522
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** PostHog
- **Affected Products:** PostHog
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-097/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of PostHog. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the database_schema method. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

PostHog has issued an update to correct this vulnerability. More details can be found at: https://github.com/PostHog/posthog/commit/3732c0fd9551ed29521b58611bf1e44d918c1032

## Disclosure Timeline

- 2024-10-03 - Vulnerability reported to vendor
- 2025-02-25 - Coordinated public release of advisory
- 2025-02-25 - Advisory Updated
