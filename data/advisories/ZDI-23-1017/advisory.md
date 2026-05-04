# ZDI-23-1017: Extreme Networks AP410C Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1017
- **ZDI-CAN:** ZDI-CAN-19695
- **Date:** 2023-08-04
- **CVE:** CVE-2023-35803
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Extreme Networks
- **Affected Products:** AP410C
- **Credit:** Victorien Molle - Biche T\xc3\xa9l\xc3\xa9com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1017/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Extreme Networks AP410C routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ah_acsd service, which listens on TCP port 5916 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Extreme Networks has issued an update to correct this vulnerability. More details can be found at: https://extremeportal.force.com/ExtrArticleDetail?an=000112742

## Disclosure Timeline

- 2023-07-06 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
