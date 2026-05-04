# ZDI-08-070: SonicWALL Content-Filtering Universal Script Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-070
- **ZDI-CAN:** ZDI-CAN-350
- **Date:** 2008-10-30
- **CVE:** CVE-2008-4918
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** SonicWALL
- **Affected Products:** Pro 2040
- **Credit:** Adrian 'pagvac' Pastor | GNUCITIZEN | www.gnucitizen.org
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-070/
## Vulnerability Details

This vulnerability allows remote attackers to execute a script injection attack on arbitrary sites through vulnerable installations of SonicWALL. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page or open a malicious web link. The specific flaw exists in the default error page displayed when a user requests access to a web site that is blocked based on the devices content-filtering rules. Insufficient sanity checks allow an attacker to craft a URL that will trigger an error and simultaneously inject a malicious script. As the browser is unable to differentiate between content delivered from the original top level site requested and the inline device, the script injection occurs under the context of the target domain. This can result in various further compromise.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: http://www.sonicwall.com/downloads/SonicOS_Enhanced_4.0.1.1_Release_Notes.pdf

## Disclosure Timeline

- 2008-06-25 - Vulnerability reported to vendor
- 2008-10-30 - Coordinated public release of advisory
