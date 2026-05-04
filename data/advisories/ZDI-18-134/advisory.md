# ZDI-18-134: (0Day) Belkin Wemo Link and Smart Plug UPNP changeFriendlyName Buffer Overflow Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-134
- **ZDI-CAN:** ZDI-CAN-5206
- **Date:** 2018-01-23
- **CVE:** N/A
- **CVSS:** 6.1
- **CVSS Vector:** AV:A/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Belkin
- **Affected Products:** Wemo Link
- **Credit:** Dove Chiu of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-134/
## Vulnerability Details

This vulnerability allows attackers on the local network to create a denial-of-service condition on the Belkin Wemo Link and Smart Plug device, despite factory resets. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of XML parsing in the UPNP service. When parsing changeFriendlyName requests, the process does not properly validate the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to trigger an infinite reboot loop and deny service to users of the device.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 09/07/17 - ZDI reported vulnerability to vendor 01/18/18 - ZDI notified the vendor the intention to 0-day the case -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2017-09-08 - Vulnerability reported to vendor
- 2018-01-23 - Coordinated public release of advisory
