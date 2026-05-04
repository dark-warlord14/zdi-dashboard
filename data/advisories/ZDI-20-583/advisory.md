# ZDI-20-583: Trading Technologies X_TRADER unblock_proxy_site Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-583
- **ZDI-CAN:** ZDI-CAN-9970
- **Date:** 2020-05-06
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trading Technologies
- **Affected Products:** X_TRADER
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-583/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trading Technologies X_TRADER. Authentication is not required to exploit this vulnerability. The specific flaw exists within the messaging daemon. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

TT has released an updated TTM package 7.1.28.3 addressing these reports. Release notes: https://download.tradingtechnologies.com/File/Detail/29199

## Disclosure Timeline

- 2020-01-16 - Vulnerability reported to vendor
- 2020-05-06 - Coordinated public release of advisory
