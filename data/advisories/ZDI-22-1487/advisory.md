# ZDI-22-1487: Delta Industrial Automation InfraSuite Device Master DeSerializeBinary Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1487
- **ZDI-CAN:** ZDI-CAN-17701
- **Date:** 2022-10-27
- **CVE:** CVE-2022-41779
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1487/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation InfraSuite Device Master Device-Monitor. User interaction is required to exploit this vulnerability in that the target client must connect to a malicious server. The specific flaw exists within the DeSerializeBinary function. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-298-07

## Disclosure Timeline

- 2022-06-28 - Vulnerability reported to vendor
- 2022-10-27 - Coordinated public release of advisory
