# ZDI-23-162: Microsoft Exchange MultiValuedProperty Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-162
- **ZDI-CAN:** ZDI-CAN-18985
- **Date:** 2023-02-24
- **CVE:** CVE-2023-21529
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-162/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the MultiValuedProperty class. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21529

## Disclosure Timeline

- 2022-09-29 - Vulnerability reported to vendor
- 2023-02-24 - Coordinated public release of advisory
