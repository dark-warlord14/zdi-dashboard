# ZDI-20-1393: Apple macOS libnetworkextension ne_filter_protocol_remove_input_handler Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1393
- **ZDI-CAN:** ZDI-CAN-11457
- **Date:** 2020-12-03
- **CVE:** CVE-2020-9996
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Zhiwei Yuan of Trend Micro iCore Team, Junzhi Lu and Mickey Jin of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1393/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of network extensions in PDFs. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211931

## Disclosure Timeline

- 2020-07-02 - Vulnerability reported to vendor
- 2020-12-03 - Coordinated public release of advisory
