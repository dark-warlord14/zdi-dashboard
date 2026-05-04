# ZDI-24-1516: Trend Micro Deep Security Agent Manual Scan Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1516
- **ZDI-CAN:** ZDI-CAN-25215
- **Date:** 2024-11-19
- **CVE:** CVE-2024-51503
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Deep Security
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1516/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Deep Security Agent. Authentication is required to exploit this vulnerability. The specific flaw exists within the Trend Micro Deep Security Notifier service. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0018154

## Disclosure Timeline

- 2024-08-20 - Vulnerability reported to vendor
- 2024-11-19 - Coordinated public release of advisory
- 2024-11-19 - Advisory Updated
