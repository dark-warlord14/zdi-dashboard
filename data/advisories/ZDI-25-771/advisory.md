# ZDI-25-771: Trend Micro Apex One Console Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-771
- **ZDI-CAN:** ZDI-CAN-27834
- **Date:** 2025-08-05
- **CVE:** CVE-2025-54948
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Jacky Hsieh @ CoreCloud Tech
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-771/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Apex One. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Apex One console, which listens on TCP ports 8080 and 4343 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of IUSR.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0020652

## Disclosure Timeline

- 2025-08-01 - Vulnerability reported to vendor
- 2025-08-05 - Coordinated public release of advisory
- 2025-08-05 - Advisory Updated
