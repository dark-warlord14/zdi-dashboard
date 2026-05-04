# ZDI-26-109: Bosch Rexroth IndraWorks OPC.TestClient XML File Parsing Deserialization Of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-109
- **ZDI-CAN:** ZDI-CAN-27994
- **Date:** 2026-02-19
- **CVE:** CVE-2025-60035
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bosch Rexroth
- **Affected Products:** IndraWorks
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-109/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Bosch Rexroth IndraWorks. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XML files in the OPC.TestClient component. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Bosch Rexroth has issued an update to correct this vulnerability. More details can be found at: https://www.boschrexroth.com/en/de/company/product-security/security-advisories/

## Disclosure Timeline

- 2025-10-09 - Vulnerability reported to vendor
- 2026-02-19 - Coordinated public release of advisory
- 2026-02-19 - Advisory Updated
