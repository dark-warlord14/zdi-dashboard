# ZDI-15-555: SolarWinds DameWare Mini Remote Control URI Handler Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-555
- **ZDI-CAN:** ZDI-CAN-3125
- **Date:** 2015-11-10
- **CVE:** CVE-2015-8220
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SolarWinds
- **Affected Products:** DameWare Mini Remote Control
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-555/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds DameWare Mini Remote Control. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within DWRCC.exe. By crafting a malicious link, an attacker can trigger a stack buffer overflow while parsing the command-line arguments. This vulnerability could be used to execute arbitrary code in the context of the browser.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://thwack.solarwinds.com/message/308973

## Disclosure Timeline

- 2015-09-29 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
