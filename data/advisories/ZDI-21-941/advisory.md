# ZDI-21-941: Apple macOS libType1Scaler PFB Font Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-941
- **ZDI-CAN:** ZDI-CAN-13268
- **Date:** 2021-08-05
- **CVE:** CVE-2021-30759
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** hjy79425575
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-941/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the libType1Scaler library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of PFB fonts. A crafted PFB font can trigger an overflow of a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212602

## Disclosure Timeline

- 2021-05-05 - Vulnerability reported to vendor
- 2021-08-05 - Coordinated public release of advisory
