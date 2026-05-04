# ZDI-20-263: (0Day) WECON LeviStudioU G_bmp szFilename Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-263
- **ZDI-CAN:** ZDI-CAN-9290
- **Date:** 2020-02-20
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** LeviStudioU
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-263/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Wecon LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XML files. When parsing the szFilename attribute of the G_bmp element, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 09/26/19 – ZDI provided the vulnerability reports to ICS-CERT 09/26/19 – ICS-CERT acknowledged the reports and provided an ICS-VU# 01/24/20 – ZDI requested any available update about the reports 01/24/20 – ICS-CERT indicated the vendor had acknowledged the reports, but that no further update was available 02/05/20 - ZDI requested any available update about the reports 02/06/20 – ICS-CERT replied that there was no update available 02/10/20 – ZDI notified ICS-CERT of the intent to publish the reports as 0-day on 02/20/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-09-26 - Vulnerability reported to vendor
- 2020-02-20 - Coordinated public release of advisory
