# ZDI-18-1337: Losant Arduino MQTT Client Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1337
- **ZDI-CAN:** ZDI-CAN-6436
- **Date:** 2018-11-02
- **CVE:** CVE-2018-17614
- **CVSS:** 5.4
- **CVSS Vector:** AV:A/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Losant
- **Affected Products:** Arduino MQTT Client
- **Credit:** Federico "phretor" Maggi of Trend Micro Security Research and Davide "_ocean" Quarta
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1337/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Losant Arduino MQTT Client. User interaction is not required to exploit this vulnerability. The specific flaw exists within the parsing of MQTT PUBLISH packets. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Losant has issued an update to correct this vulnerability. More details can be found at: https://github.com/knolleary/pubsubclient/releases/tag/v2.7

## Disclosure Timeline

- 2018-07-18 - Vulnerability reported to vendor
- 2018-11-02 - Coordinated public release of advisory
- 2018-11-02 - Advisory Updated
