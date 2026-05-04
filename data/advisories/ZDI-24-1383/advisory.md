# ZDI-24-1383: PostHog database_schema Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1383
- **ZDI-CAN:** ZDI-CAN-25351
- **Date:** 2024-10-15
- **CVE:** CVE-2024-9710
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** PostHog
- **Affected Products:** PostHog
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1383/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of PostHog. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the database_schema method. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

PostHog has issued an update to correct this vulnerability. More details can be found at: https://github.com/PostHog/posthog/pull/25388

## Disclosure Timeline

- 2024-10-03 - Vulnerability reported to vendor
- 2024-10-15 - Coordinated public release of advisory
- 2024-10-15 - Advisory Updated
