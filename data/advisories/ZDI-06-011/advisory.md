# ZDI-06-011: Mozilla Firefox Table Rebuilding Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-011
- **ZDI-CAN:** ZDI-CAN-026
- **Date:** 2006-04-25
- **CVE:** CVE-2006-0748
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 1.5.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-011/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of the Mozilla/Firefox web browser and Thunderbird e-mail client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious e-mail. The specific flaw exists within the routine RebuildConsideringRows() during the rebuilding of nonsensical table tags. When the Mozilla engine attempts to fix the malformed table, an attacker is capable of triggering a memory corruption that can lead to code execution from user-supplied data.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2006/mfsa2006-27.html

## Disclosure Timeline

- 2006-02-28 - Vulnerability reported to vendor
- 2006-04-25 - Coordinated public release of advisory
