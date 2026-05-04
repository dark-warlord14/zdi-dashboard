# ZDI-24-1418: Trend Micro Cloud Edge REST API Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1418
- **ZDI-CAN:** ZDI-CAN-23182
- **Date:** 2024-10-17
- **CVE:** CVE-2024-48904
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Cloud Edge
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1418/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Cloud Edge. Authentication is not required to exploit this vulnerability. The specific flaw exists within the REST API, which listens on TCP port 8443 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0017998

## Disclosure Timeline

- 2024-02-06 - Vulnerability reported to vendor
- 2024-10-17 - Coordinated public release of advisory
- 2024-10-17 - Advisory Updated
