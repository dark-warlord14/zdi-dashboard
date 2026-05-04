# ZDI-22-1654: Microsoft Exchange DagNetMultiValuedProperty Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1654
- **ZDI-CAN:** ZDI-CAN-18986
- **Date:** 2022-11-22
- **CVE:** CVE-2022-41082
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1654/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the DagNetMultiValuedProperty class. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082

## Disclosure Timeline

- 2022-09-29 - Vulnerability reported to vendor
- 2022-11-22 - Coordinated public release of advisory
