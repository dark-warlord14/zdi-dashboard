# ZDI-22-372: Trend Micro Apex One Security Agent Resource Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-372
- **ZDI-CAN:** ZDI-CAN-15047
- **Date:** 2022-02-16
- **CVE:** CVE-2022-24678
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Elias Martinez (filenotfound - https://www.linkedin.com/in/eli-martinez07/)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-372/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Trend Micro Apex One Security Agent. Authentication is not required to exploit this vulnerability. The specific flaw exists within the logging of requests received on the management port. By sending a large number of requests, an attacker can cause log files to grow without limit. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000290464

## Disclosure Timeline

- 2021-10-27 - Vulnerability reported to vendor
- 2022-02-16 - Coordinated public release of advisory
