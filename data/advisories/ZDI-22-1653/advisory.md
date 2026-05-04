# ZDI-22-1653: Microsoft Exchange FileHandler Exposed Dangerous Function Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1653
- **ZDI-CAN:** ZDI-CAN-18972
- **Date:** 2022-11-22
- **CVE:** CVE-2022-41082
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1653/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the FileHandler class. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082

## Disclosure Timeline

- 2022-10-04 - Vulnerability reported to vendor
- 2022-11-22 - Coordinated public release of advisory
