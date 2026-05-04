# ZDI-23-1420: Microsoft Exchange DumpDataReader Deserialization of Untrusted Data Arbitrary File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1420
- **ZDI-CAN:** ZDI-CAN-21614
- **Date:** 2023-09-12
- **CVE:** CVE-2023-36744
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1420/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the lack of protection against deserialization of the DumpDataReader class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36744

## Disclosure Timeline

- 2023-07-11 - Vulnerability reported to vendor
- 2023-09-12 - Coordinated public release of advisory
