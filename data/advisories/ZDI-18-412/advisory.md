# ZDI-18-412: Trend Micro Encryption for Email Gateway Registration Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-412
- **ZDI-CAN:** ZDI-CAN-5532
- **Date:** 2018-05-04
- **CVE:** CVE-2018-6223
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Encryption for Email Gateway
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-412/
## Vulnerability Details

This vulnerability allows remote attackers to reset the Administrator password on vulnerable installations of Trend Micro Encryption for Email Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the product registration process. The issue results from the lack of validating the product registration status prior to performing product registration. An attacker can leverage this vulnerability to reset the Administrator password.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119349

## Disclosure Timeline

- 2018-01-02 - Vulnerability reported to vendor
- 2018-05-04 - Coordinated public release of advisory
- 2018-05-04 - Advisory Updated
