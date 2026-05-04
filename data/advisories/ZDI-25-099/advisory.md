# ZDI-25-099: PostHog ClickHouse Table Functions SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-099
- **ZDI-CAN:** ZDI-CAN-25350
- **Date:** 2025-02-25
- **CVE:** CVE-2025-1520
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** PostHog
- **Affected Products:** PostHog
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-099/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of PostHog. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the SQL parser. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the database account.

## Additional Details

PostHog has issued an update to correct this vulnerability. More details can be found at: https://github.com/PostHog/posthog/commit/6e8f035f9acd339c5ba87ba6ea40fc1ab3053d42

## Disclosure Timeline

- 2024-10-03 - Vulnerability reported to vendor
- 2025-02-25 - Coordinated public release of advisory
- 2025-02-25 - Advisory Updated
